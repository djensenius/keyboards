# Clickety Split Ltd. | Pepito-Macro

## Keyboard Layout

This document shows the key mappings for each layer of the Pepito-Macro split keyboard.

**Legend:**
- `▽` = Transparent (uses lower layer)
- `✗` = None (no action)
- `MO(X)` = Momentary layer activation
- `LT(X,key)` = Layer tap (hold for layer, tap for key)
- `CTRL+key` = Homerow mod (hold for modifier, tap for key)

### OS Keyboard Layout Support

This keyboard layout is designed to work with both QWERTY and Colemak layouts at the OS level:

- **QWERTY**: Use the standard QWERTY layout in your OS settings
- **Colemak**: Switch your OS to Colemak layout - the physical key bindings remain the same, but your OS will interpret them as Colemak characters

The layers shown below display the physical key positions. When using Colemak at the OS level, the home row will effectively become: **A R S T D** (left) and **H N E I O** (right).

### Main Layer (QWERTY)

<details>
<summary>Click to expand QWERTY layout</summary>

```
+-----------------------------------------------+    +-----------------------------------------------+
|                   LEFT HALF                   |    |                   RIGHT HALF                  |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   ⇥   |   Q   |   W   |   E   |   R   |   T   |    |   Y   |   U   |   I   |   O   |   P   |   \   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   ⎋   | CT+A  | AT+S  |   D   | GM+F  |   G   |    |   H   | GM+J  |   K   | AT+L  | CT+;  |   '   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   ⇧   |   Z   |   X   |   C   |   V   |   B   |    |   N   |   M   |   ,   |   .   |   /   |   ⇧   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
                        |  M:F  |  M:A  |                        |  M:A  |  M:F  |
                        +-------+-------+                        +-------+-------+
                        |   ␣   |  N:⏎  |                        |  N:⌦  |   ⌫   |
                        +-------+-------+                        +-------+-------+
```

</details>

### Lower Layer (Navigation)

```
+-----------------------------------------------+    +-----------------------------------------------+
|                   LEFT HALF                   |    |                   RIGHT HALF                  |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   ▽   |   ✗   |  F7   |  F8   |  F9   |   ✗   |    | LFT2  | LFT1  | RGT1  | RGT2  | VOL+  |   ▽   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   ▽   | CT+BR | AT+F4 |  F5   | GM+F6 |  BR+  |    |   ←   |   ↓   |   ↑   |   →   | VOL-  |   ▽   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   ▽   | LGUI  |  F1   |  F2   |  F3   | RGUI  |    |   ⤴   |   ⇟   |   ⇞   |   ⤵   |   ⇪   |   ▽   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
                        |   ▽   |   ▽   |                        |   ▽   |   ▽   |
                        +-------+-------+                        +-------+-------+
                        |   ▽   |   ▽   |                        |   ▽   |   ▽   |
                        +-------+-------+                        +-------+-------+
```

### Raise Layer (Numbers)

```
+-----------------------------------------------+    +-----------------------------------------------+
|                   LEFT HALF                   |    |                   RIGHT HALF                  |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   -   |   1   |   2   |   3   |   4   |   5   |    |   6   |   7   |   8   |   9   |   0   |   =   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   ▽   | CT+OS | AT+LN | FIND  | GM+CL |   ▽   |    |   ←   |   ↓   |   ↑   |   →   |   ▽   |   ▽   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   ▽   | LGUI  |   ▽   |   ▽   |   ▽   | RGUI  |    |   ⤴   |   ⇟   |   ⇞   |   ⤵   |   ▽   |   ▽   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
                        |   ▽   |   ▽   |                        |   ⌦   |   ▽   |
                        +-------+-------+                        +-------+-------+
                        |   ▽   |   ▽   |                        |   ▽   |   ▽   |
                        +-------+-------+                        +-------+-------+
```

### Adjust Layer (Function Keys)

```
+-----------------------------------------------+    +-----------------------------------------------+
|                   LEFT HALF                   |    |                   RIGHT HALF                  |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   ▽   |  F1   |  F2   |  F3   |  F4   |  F5   |    |   ✗   |   ✗   | VOL+  |   ✗   |   ✗   |   ✗   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   ▽   | CT+F6 | AT+F7 |  F8   | GM+F9 |  F10  |    |   ✗   | VOL-  | VOL+  | LOCK  |   ✗   |   ✗   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   ▽   |  F11  |  F12  |   ✗   |   ✗   |   ✗   |    |   ✗   | MUTE  |   ✗   |   ✗   |   ✗   |   ▽   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
                        |   ▽   |   ▽   |                        |   ▽   |   ▽   |
                        +-------+-------+                        +-------+-------+
                        |   ▽   |   ▽   |                        |   ▽   |   ▽   |
                        +-------+-------+                        +-------+-------+
```

### Firmware Layer (Bluetooth)

```
+-----------------------------------------------+    +-----------------------------------------------+
|                   LEFT HALF                   |    |                   RIGHT HALF                  |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   ✗   |  BT0  |  BT1  |  BT2  |  BT3  |  BT4  |    |  BT0  |  BT1  |  BT2  |  BT3  |  BT4  |   ✗   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   ✗   | BOOT  |  RST  |   ✗   |   ✗   |   ✗   |    |   ✗   |   ✗   |   ✗   |  RST  | BOOT  |   ✗   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
|   ✗   |   ✗   |   ✗   |   ✗   |   ✗   |   ✗   |    |   ✗   |   ✗   |   ✗   |   ✗   |   ✗   |   ✗   |
+-------+-------+-------+-------+-------+-------+    +-------+-------+-------+-------+-------+-------+
                        |   ✗   | BTCLR |                        | BTCLR |   ✗   |
                        +-------+-------+                        +-------+-------+
                        |   ▽   |   ▽   |                        |   ▽   |   ▽   |
                        +-------+-------+                        +-------+-------+
```

## Combos

Key combinations available on the main layer:

| Combo | Keys | Output |
|-------|------|--------|
| Osx Grave | ⇥ + Q | ` |
| Osx Lpar | W + E | ( |
| Osx Rpar | I + O | ) |
| Osx Lbrc | S + D | { |
| Osx Rbrc | K + L | } |
| Osx Lbkt | X + C | [ |
| Osx Rbkt | , + . | ] |
| Nav Fs | U + I | FSCR |

## Configuration Features

- ✅ Display support enabled
- ✅ WPM status widget enabled
- ⚙️ Battery percentage display disabled
- ⚙️ BLE passkey entry disabled

## Build Instructions

Build with default keymap:

```bash
west build -d build/pepito/left -p -b seeeduino_xiao_ble -- -DSHIELD=clickety_split_pepito_left
west build -d build/pepito/right -p -b seeeduino_xiao_ble -- -DSHIELD=clickety_split_pepito_right
```

Build with custom keymap:

```bash
west build -d build/pepito/left -p -b seeeduino_xiao_ble -- -DSHIELD=clickety_split_pepito_left  -DZMK_CONFIG="/workspaces/zmk-config/joey/pepito_v1.13/config"
west build -d build/pepito/right -p -b seeeduino_xiao_ble -- -DSHIELD=clickety_split_pepito_right  -DZMK_CONFIG="/workspaces/zmk-config/joey/pepito_v1.13/config"
```