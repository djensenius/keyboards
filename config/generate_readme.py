#!/usr/bin/env python3
"""
ZMK Keymap Parser and README Generator for Pepito-Macro Split Keyboard

This script parses the ZMK keymap configuration and generates a comprehensive
README with visual keyboard layout tables for all layers.
"""

import re
import os
from typing import Dict, List, Tuple, Optional

class ZMKKeymapParser:
    def __init__(self, keymap_file: str, conf_file: str):
        self.keymap_file = keymap_file
        self.conf_file = conf_file
        self.layers = {}
        self.combos = []
        self.config_features = {}
        
        # Key mappings for better readability
        self.key_symbols = {
            'TAB': '⇥',
            'ESC': '⎋',
            'SPACE': '␣',
            'RET': '⏎',
            'ENTER': '⏎',
            'DEL': '⌦',
            'BSPC': '⌫',
            'LSHFT': '⇧',
            'RSHFT': '⇧',
            'LEFT': '←',
            'RIGHT': '→',
            'UP': '↑',
            'DOWN': '↓',
            'HOME': '⤴',
            'END': '⤵',
            'PG_UP': '⇞',
            'PG_DN': '⇟',
            'CAPS': '⇪',
            'VOLUP': '🔊',
            'VOLDN': '🔉',
            'VOLMT': '🔇',
            'C_VOL_UP': '🔊',
            'C_VOL_DN': '🔉',
            'C_MUTE': '🔇',
            'TRANS': '▽',
            'NONE': '✗',
            'MINUS': '-',
            'EQUAL': '=',
            'LPAR': '(',
            'RPAR': ')',
            'LBRC': '{',
            'RBRC': '}',
            'LBKT': '[',
            'RBKT': ']',
            'SEMI': ';',
            'SQT': "'",
            'BSLH': '\\',
            'GRAV': '`',
            'COMMA': ',',
            'DOT': '.',
            'FSLH': '/',
        }
        
        # Layer names
        self.layer_names = {
            'default_osx_layer': ('Main', 'QWERTY'),
            'lower_osx_layer': ('Lower', 'Navigation'),
            'raise_osx_layer': ('Raise', 'Numbers'),
            'adjust_osx_layer': ('Adjust', 'Function Keys'),
            'firmware_layer': ('Firmware', 'Bluetooth'),
        }
    
    def parse_keymap(self):
        """Parse the ZMK keymap file and extract layer definitions."""
        with open(self.keymap_file, 'r') as f:
            content = f.read()
        
        # Parse layer definitions
        layer_pattern = r'(\w+_layer)\s*\{[^}]*?label\s*=\s*"([^"]*)"[^}]*?bindings\s*=\s*<([^>]*)>'
        for match in re.finditer(layer_pattern, content, re.DOTALL):
            layer_name, label, bindings = match.groups()
            keys = self._parse_bindings(bindings)
            self.layers[layer_name] = {
                'label': label.strip(),
                'keys': keys
            }
        
        # Parse combos
        combo_pattern = r'combo_(\w+)\s*\{[^}]*?key-positions\s*=\s*<([^>]*)>[^}]*?bindings\s*=\s*<([^>]*)>'
        for match in re.finditer(combo_pattern, content, re.DOTALL):
            combo_name, positions, binding = match.groups()
            positions_list = [int(x.strip()) for x in positions.split()]
            output = self._parse_binding(binding.strip())
            self.combos.append({
                'name': combo_name,
                'positions': positions_list,
                'binding': binding.strip(),
                'keys': self._get_combo_keys(positions_list),
                'output': output
            })
    
    def parse_config(self):
        """Parse the configuration file for features."""
        with open(self.conf_file, 'r') as f:
            lines = f.readlines()
        
        features = {
            'CONFIG_ZMK_DISPLAY': ('Display support', False),
            'CONFIG_ZMK_WIDGET_WPM_STATUS': ('WPM status widget', False),
            'CONFIG_ZMK_WIDGET_BATTERY_STATUS_SHOW_PERCENTAGE': ('Battery percentage display', False),
            'CONFIG_ZMK_BLE_PASSKEY_ENTRY': ('BLE passkey entry', False),
        }
        
        for line in lines:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            
            for config_key, (description, default) in features.items():
                if line.startswith(config_key):
                    value = line.split('=')[1] if '=' in line else 'y'
                    enabled = value.strip().lower() == 'y'
                    self.config_features[description] = enabled
    
    def _parse_bindings(self, bindings_str: str) -> List[str]:
        """Parse binding string into individual key bindings."""
        # Remove whitespace and split by & (binding separator)
        bindings = re.sub(r'\s+', ' ', bindings_str.strip())
        keys = []
        
        # Split by & but handle complex bindings
        for binding in re.split(r'&(?![^<]*>)', bindings):
            binding = binding.strip()
            if binding:
                keys.append(self._parse_binding(binding))
        
        return keys
    
    def _parse_binding(self, binding: str) -> str:
        """Parse a single key binding into readable format."""
        binding = binding.strip()
        
        # Handle different binding types
        if binding.startswith('kp '):
            key = binding[3:].strip()
            return self.key_symbols.get(key, key)
        elif binding.startswith('hm '):
            # Homerow mod: hm LCTRL A -> CTRL+A
            parts = binding[3:].split()
            if len(parts) >= 2:
                mod = parts[0].replace('L', '').replace('R', '')
                key = parts[1]
                key_symbol = self.key_symbols.get(key, key)
                return f"{mod}+{key_symbol}"
            return binding
        elif binding.startswith('lt '):
            # Layer tap: lt 1 RET -> LT(NAV,⏎)
            parts = binding[3:].split()
            if len(parts) >= 2:
                layer_num = parts[0]
                key = parts[1]
                layer_name = self._get_layer_name_by_number(layer_num)
                key_symbol = self.key_symbols.get(key, key)
                return f"LT({layer_name},{key_symbol})"
            return binding
        elif binding.startswith('mo '):
            # Momentary layer: mo QX_A -> MO(ADJ)
            layer = binding[3:].strip()
            layer_name = self._get_layer_name(layer)
            return f"MO({layer_name})"
        elif binding.startswith('bt '):
            # Bluetooth: bt BT0 -> BT0
            return binding[3:].strip()
        elif binding.startswith('&kp '):
            key = binding[4:].strip()
            return self.key_symbols.get(key, key)
        elif binding.startswith('&hm '):
            # Homerow mod: &hm LCTRL A -> CTRL+A
            parts = binding[4:].split()
            if len(parts) >= 2:
                mod = parts[0].replace('L', '').replace('R', '')
                key = parts[1]
                key_symbol = self.key_symbols.get(key, key)
                return f"{mod}+{key_symbol}"
            return binding
        elif binding.startswith('&lt '):
            # Layer tap: &lt 1 RET -> LT(NAV,⏎)
            parts = binding[4:].split()
            if len(parts) >= 2:
                layer_num = parts[0]
                key = parts[1]
                layer_name = self._get_layer_name_by_number(layer_num)
                key_symbol = self.key_symbols.get(key, key)
                return f"LT({layer_name},{key_symbol})"
            return binding
        elif binding.startswith('&mo '):
            # Momentary layer: &mo QX_A -> MO(ADJ)
            layer = binding[4:].strip()
            layer_name = self._get_layer_name(layer)
            return f"MO({layer_name})"
        elif binding.startswith('&bt '):
            # Bluetooth: &bt BT0 -> BT0
            return binding[4:].strip()
        elif binding == 'trans' or binding == '&trans':
            return '▽'
        elif binding == 'none' or binding == '&none':
            return '✗'
        elif binding == 'BOOTLDR' or binding == '&bootloader':
            return 'BOOT'
        elif binding == 'SYSRSET' or binding == '&sys_reset':
            return 'RESET'
        elif binding == '&bt BT_CLR':
            return 'BT_CLR'
        elif binding.startswith('&'):
            # Remove & prefix and try again
            return self._parse_binding(binding[1:])
        else:
            # Handle other cases
            return self.key_symbols.get(binding, binding)
    
    def _get_layer_name(self, layer_code: str) -> str:
        """Convert layer code to readable name."""
        layer_map = {
            'QX_M': 'MAIN', '0': 'MAIN',
            'QX_L': 'NAV', '1': 'NAV',
            'QX_R': 'NUM', '2': 'NUM',
            'QX_A': 'ADJ', '3': 'ADJ',
            'QC_F': 'FW', '4': 'FW'
        }
        return layer_map.get(layer_code, layer_code)
    
    def _get_layer_name_by_number(self, num: str) -> str:
        """Get layer name by number."""
        return self._get_layer_name(num)
    
    def _get_combo_keys(self, positions: List[int]) -> str:
        """Get key names for combo positions based on the default layer."""
        if 'default_osx_layer' not in self.layers:
            return " + ".join([f"pos{p}" for p in positions])
        
        default_keys = self.layers['default_osx_layer']['keys']
        key_names = []
        
        for pos in positions:
            if pos < len(default_keys):
                key = default_keys[pos]
                # Clean up the key name for display
                if '+' in key:
                    # For homerow mods, just show the base key
                    key = key.split('+')[-1]
                key_names.append(key)
            else:
                key_names.append(f"pos{pos}")
        
        return " + ".join(key_names)
    
    def generate_layer_table(self, layer_name: str, layer_data: Dict) -> str:
        """Generate markdown table for a layer with improved visual layout."""
        keys = layer_data['keys']
        if len(keys) < 44:
            keys.extend(['✗'] * (44 - len(keys)))
        
        # The keymap has 12 keys per row (6 left + 6 right) for 3 rows (36 keys)
        # Plus 8 thumb keys (4 left + 4 right)
        # Layout: row1(12) + row2(12) + row3(12) + thumbs(8) = 44 keys total
        
        # Extract rows: each row has 12 keys (6 left + 6 right)
        row1 = keys[0:12]   # TAB Q W E R T | Y U I O P BSLH
        row2 = keys[12:24]  # ESC A S D F G | H J K L ; SQT
        row3 = keys[24:36]  # SHFT Z X C V B | N M , . / SHFT
        thumbs = keys[36:44] if len(keys) >= 44 else keys[36:] + ['✗'] * (8 - (len(keys) - 36))
        
        # Split each row into left and right halves
        left_row1, right_row1 = row1[:6], row1[6:]
        left_row2, right_row2 = row2[:6], row2[6:]
        left_row3, right_row3 = row3[:6], row3[6:]
        left_thumbs, right_thumbs = thumbs[:4], thumbs[4:]
        
        # Generate the table with better visual representation
        table = []
        table.append("```")
        table.append("╭─────────────────────────────────────╮    ╭─────────────────────────────────────╮")
        table.append("│               LEFT HALF              │    │              RIGHT HALF             │")
        table.append("├─────┬─────┬─────┬─────┬─────┬─────────┤    ├─────────┬─────┬─────┬─────┬─────┬─────┤")
        
        # Format keys with proper width for readability
        def format_key(key):
            if len(str(key)) > 4:
                return str(key)[:4]
            return str(key)
        
        # Row 1
        left_formatted = '│'.join([f" {format_key(key):^4} " for key in left_row1])
        right_formatted = '│'.join([f" {format_key(key):^4} " for key in right_row1])
        table.append(f"│{left_formatted}│    │{right_formatted}│")
        
        table.append("├─────┼─────┼─────┼─────┼─────┼─────────┤    ├─────────┼─────┼─────┼─────┼─────┼─────┤")
        
        # Row 2
        left_formatted = '│'.join([f" {format_key(key):^4} " for key in left_row2])
        right_formatted = '│'.join([f" {format_key(key):^4} " for key in right_row2])
        table.append(f"│{left_formatted}│    │{right_formatted}│")
        
        table.append("├─────┼─────┼─────┼─────┼─────┼─────────┤    ├─────────┼─────┼─────┼─────┼─────┼─────┤")
        
        # Row 3
        left_formatted = '│'.join([f" {format_key(key):^4} " for key in left_row3])
        right_formatted = '│'.join([f" {format_key(key):^4} " for key in right_row3])
        table.append(f"│{left_formatted}│    │{right_formatted}│")
        
        table.append("╰─────┴─────┴─────┼─────┼─────┼─────────╯    ╰─────────┼─────┼─────┼─────┴─────┴─────╯")
        table.append("                  │ {:^4} │ {:^4} │                      │ {:^4} │ {:^4} │".format(
            format_key(left_thumbs[0]), format_key(left_thumbs[1]), 
            format_key(right_thumbs[2]), format_key(right_thumbs[3])
        ))
        table.append("                  ├─────┼─────┤                      ├─────┼─────┤")
        table.append("                  │ {:^4} │ {:^4} │                      │ {:^4} │ {:^4} │".format(
            format_key(left_thumbs[2]), format_key(left_thumbs[3]), 
            format_key(right_thumbs[0]), format_key(right_thumbs[1])
        ))
        table.append("                  ╰─────┴─────╯                      ╰─────┴─────╯")
        table.append("```")
        
        return "\n".join(table)
    
    def generate_readme(self) -> str:
        """Generate the complete README content."""
        self.parse_keymap()
        self.parse_config()
        
        readme = []
        readme.append("# Clickety Split Ltd. | Pepito-Macro")
        readme.append("")
        readme.append("## Keyboard Layout")
        readme.append("")
        readme.append("This document shows the key mappings for each layer of the Pepito-Macro split keyboard.")
        readme.append("")
        readme.append("**Legend:**")
        readme.append("- `▽` = Transparent (uses lower layer)")
        readme.append("- `✗` = None (no action)")
        readme.append("- `MO(X)` = Momentary layer activation")
        readme.append("- `LT(X,key)` = Layer tap (hold for layer, tap for key)")
        readme.append("- `CTRL+key` = Homerow mod (hold for modifier, tap for key)")
        readme.append("")
        
        # Generate layer tables
        for layer_name, layer_data in self.layers.items():
            if layer_name in self.layer_names:
                title, subtitle = self.layer_names[layer_name]
                readme.append(f"### {title} Layer ({subtitle})")
                readme.append("")
                readme.append(self.generate_layer_table(layer_name, layer_data))
                readme.append("")
        
        # Add combos section
        if self.combos:
            readme.append("## Combos")
            readme.append("")
            readme.append("Key combinations available on the main layer:")
            readme.append("")
            readme.append("| Combo | Keys | Output |")
            readme.append("|-------|------|--------|")
            
            for combo in self.combos:
                combo_name = combo['name'].replace('_', ' ').title()
                readme.append(f"| {combo_name} | {combo['keys']} | {combo['output']} |")
            
            readme.append("")
        
        # Add configuration features
        if self.config_features:
            readme.append("## Configuration Features")
            readme.append("")
            for feature, enabled in self.config_features.items():
                status = "✅" if enabled else "⚙️"
                state = "enabled" if enabled else "disabled"
                readme.append(f"- {status} {feature} {state}")
            readme.append("")
        
        # Add build instructions
        readme.append("## Build Instructions")
        readme.append("")
        readme.append("Build with default keymap:")
        readme.append("")
        readme.append("```bash")
        readme.append("west build -d build/pepito/left -p -b seeeduino_xiao_ble -- -DSHIELD=clickety_split_pepito_left")
        readme.append("west build -d build/pepito/right -p -b seeeduino_xiao_ble -- -DSHIELD=clickety_split_pepito_right")
        readme.append("```")
        readme.append("")
        readme.append("Build with custom keymap:")
        readme.append("")
        readme.append("```bash")
        readme.append("west build -d build/pepito/left -p -b seeeduino_xiao_ble -- -DSHIELD=clickety_split_pepito_left  -DZMK_CONFIG=\"/workspaces/zmk-config/joey/pepito_v1.13/config\"")
        readme.append("west build -d build/pepito/right -p -b seeeduino_xiao_ble -- -DSHIELD=clickety_split_pepito_right  -DZMK_CONFIG=\"/workspaces/zmk-config/joey/pepito_v1.13/config\"")
        readme.append("```")
        
        return "\n".join(readme)

def main():
    """Main function to generate the README."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    keymap_file = os.path.join(script_dir, 'clickety_split_pepito.keymap')
    conf_file = os.path.join(script_dir, 'clickety_split_pepito.conf')
    readme_file = os.path.join(script_dir, 'readme.md')
    
    if not os.path.exists(keymap_file):
        print(f"Error: {keymap_file} not found")
        return
    
    if not os.path.exists(conf_file):
        print(f"Error: {conf_file} not found")
        return
    
    parser = ZMKKeymapParser(keymap_file, conf_file)
    readme_content = parser.generate_readme()
    
    with open(readme_file, 'w') as f:
        f.write(readme_content)
    
    print(f"Generated {readme_file}")

if __name__ == "__main__":
    main()