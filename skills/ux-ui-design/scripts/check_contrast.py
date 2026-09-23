"""
WCAG 2.1 Color Contrast Ratio Checker
--------------------------------------
Calculates contrast ratio between text color and background color
according to W3C WCAG 2.1 specifications.

Usage:
    python check_contrast.py "#18181B" "#FFFFFF"
    python check_contrast.py "#2563EB" "#FFFFFF"
"""

import sys

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    if len(hex_str) == 3:
        hex_str = ''.join(c * 2 for c in hex_str)
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def get_luminance(r, g, b):
    # sRGB to linear RGB conversion
    def channel_lum(val):
        v = val / 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    
    r_lin = channel_lum(r)
    g_lin = channel_lum(g)
    b_lin = channel_lum(b)
    return 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin

def contrast_ratio(color1_hex, color2_hex):
    rgb1 = hex_to_rgb(color1_hex)
    rgb2 = hex_to_rgb(color2_hex)
    
    lum1 = get_luminance(*rgb1)
    lum2 = get_luminance(*rgb2)
    
    brightest = max(lum1, lum2)
    darkest = min(lum1, lum2)
    
    return (brightest + 0.05) / (darkest + 0.05)

def main():
    if len(sys.argv) < 3:
        print("Ishlatish: python check_contrast.py <rang1_hex> <rang2_hex>")
        print("Misol:     python check_contrast.py \"#18181B\" \"#FFFFFF\"")
        sys.exit(1)
        
    c1, c2 = sys.argv[1], sys.argv[2]
    ratio = contrast_ratio(c1, c2)
    
    print("\n=== WCAG 2.1 Kontrast Tahlili ===")
    print(f"Rang 1 (Matn):     {c1}")
    print(f"Rang 2 (Orqa fon): {c2}")
    print(f"Kontrast nisbati:  {ratio:.2f}:1")
    print("---------------------------------")
    
    # Standartlar
    aa_normal = ratio >= 4.5
    aa_large  = ratio >= 3.0
    aaa_normal = ratio >= 7.0
    
    print(f"WCAG AA (Oddiy matn, min 4.5:1): {'PASSED' if aa_normal else 'FAILED'}")
    print(f"WCAG AA (Katta matn / UI, min 3.0:1): {'PASSED' if aa_large else 'FAILED'}")
    print(f"WCAG AAA (Yuqori daraja, min 7.0:1): {'PASSED' if aaa_normal else 'FAILED'}")
    print("=================================\n")

if __name__ == "__main__":
    main()
