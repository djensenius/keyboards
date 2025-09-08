# Clickety Split Ltd. | Pepito-Macro

## Keyboard Layout

This document shows the key mappings for each layer of the Pepito-Macro split keyboard.

**Legend:**
- `▽` = Transparent (uses lower layer)
- `✗` = None (no action)
- `MO(X)` = Momentary layer activation
- `LT(X,key)` = Layer tap (hold for layer, tap for key)
- `CTRL+key` = Homerow mod (hold for modifier, tap for key)

### Main Layer (QWERTY)

**Left Half** | **Right Half**
--- | ---
`⇥` `Q` `W` `E` `R` `T` | `Y` `U` `I` `O` `P` `\`
`⎋` `CTRL+A` `ALT+S` `D` `GUI+F` `G` | `H` `GUI+J` `K` `ALT+L` `CTRL+;` `'`
`⇧` `Z` `X` `C` `V` `B` | `N` `M` `,` `.` `/` `⇧`

**Thumb Keys (Left → Right):**

`MO(FW)` → `MO(ADJ)` → `␣` → `LT(NAV,⏎)` → `LT(NUM,⌦)` → `⌫` → `MO(ADJ)` → `MO(FW)`

### Lower Layer (Navigation)

**Left Half** | **Right Half**
--- | ---
`▽` `✗` `F7` `F8` `F9` `✗` | `LFT23` `LFT12` `RGT12` `RGT23` `🔊` `▽`
`▽` `CTRL+☀-` `ALT+F4` `F5` `GUI+F6` `☀+` | `←` `↓` `↑` `→` `🔉` `▽`
`▽` `LGUI` `F1` `F2` `F3` `RGUI` | `⤴` `⇟` `⇞` `⤵` `⇪` `▽`

**Thumb Keys (Left → Right):**

`▽` → `▽` → `▽` → `▽` → `▽` → `▽` → `▽` → `▽`

### Raise Layer (Numbers)

**Left Half** | **Right Half**
--- | ---
`-` `1` `2` `3` `4` `5` | `6` `7` `8` `9` `0` `=`
`▽` `CTRL+OSX_SC` `ALT+OSX_EP` `OSX_FD` `GUI+OSX_CD` `▽` | `←` `↓` `↑` `→` `▽` `▽`
`▽` `LGUI` `▽` `▽` `▽` `RGUI` | `⤴` `⇟` `⇞` `⤵` `▽` `▽`

**Thumb Keys (Left → Right):**

`▽` → `▽` → `▽` → `▽` → `▽` → `▽` → `⌦` → `▽`

### Adjust Layer (Function Keys)

**Left Half** | **Right Half**
--- | ---
`▽` `F1` `F2` `F3` `F4` `F5` | `✗` `✗` `🔊` `✗` `✗` `✗`
`▽` `CTRL+F6` `ALT+F7` `F8` `GUI+F9` `F10` | `✗` `🔉` `🔊` `LOCK_X` `✗` `✗`
`▽` `F11` `F12` `✗` `✗` `✗` | `✗` `🔇` `✗` `✗` `✗` `▽`

**Thumb Keys (Left → Right):**

`▽` → `▽` → `▽` → `▽` → `▽` → `▽` → `▽` → `▽`

### Firmware Layer (Bluetooth)

**Left Half** | **Right Half**
--- | ---
`✗` `BT0` `BT1` `BT2` `BT3` `BT4` | `BT0` `BT1` `BT2` `BT3` `BT4` `✗`
`✗` `BOOT` `RESET` `✗` `✗` `✗` | `✗` `✗` `✗` `RESET` `BOOT` `✗`
`✗` `✗` `✗` `✗` `✗` `✗` | `✗` `✗` `✗` `✗` `✗` `✗`

**Thumb Keys (Left → Right):**

`✗` → `BT_CLR` → `▽` → `▽` → `▽` → `▽` → `BT_CLR` → `✗`

## Combos

Key combinations available on the main layer:

| Combo | Keys | Output |
|-------|------|--------|
| Grave | Q + W | ` |
| Left Paren | W + E | ( |
| Right Paren | I + O | ) |
| Left Brace | S + D | { |
| Right Brace | K + L | } |
| Left Bracket | Z + X | [ |
| Right Bracket | , + . | ] |
| Fullscreen | F7 + F8 (Nav layer) | Fullscreen toggle |

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
