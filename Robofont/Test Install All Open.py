#Test Install All Open Fonts

print("Test Install All Fonts")
for font in AllFonts():
    print("  Processing", font, "...")
    font.testInstall()

print("  Done 😎")