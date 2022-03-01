## Nudge a Lot

Enable keyboard shortcuts to Nudge a lot. You can move your Tracker into 5 pixel increments.
You can also increase/decrease Tracker search area with bigger increments.
If you want to use other increment sizes, edit "pixelnudge" variable on each script.

Nudge to Prev / Next Frame Position Script (SHIFT+NUM7/CTRL+SHIFT+NUM7), will copy the last frame search box position.<br>
Nudge Key and Key Smooth Up / Down will (SHIFT+NUM1/CTRL+SHIFT+NUM1) increase/decrease the Key and Key Smooth by two fold.

[Demo video](http://www.youtube.com/watch?v=IZqyl27X7CA&feature=player_embedded)    
<a href="http://www.youtube.com/watch?feature=player_embedded&v=IZqyl27X7CA" target="_blank"><img src="http://img.youtube.com/vi/IZqyl27X7CA/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /></a>

#### Installation:
Paste this script folder into you User script folder.

Add the following lines to your keybd14.ini file (or can add whatever shortcuts on the UI you want):

keybd14.ini location:

C:\Documents and Settings\YourNameHere\Application Data\SynthEyes\keybd14.ini (Windows)<br>
/Users/YourNameHere/Library/Application Support/SynthEyes/keybd14.ini (Mac OSX) <br>
~/.SynthEyes/keybd14.ini (Linux)<br>

add these below on the end of the keybd14.ini file (these are SHIFT+ the usual movement keys on the numeric keyboard)
```
   1 Numericpad4 mb Nudge a Lot Left Script
   1 Numericpad6 mb Nudge a Lot Right Script
   1 Numericpad8 mb Nudge a Lot Up Script
   1 Numericpad2 mb Nudge a Lot Down Script
   1 Numericpad9 mb Nudge a Lot Tracker Size Up Script
   1 Numericpad3 mb Nudge a Lot Tracker Size Down Script
   1 Numericpad7 mb Nudge to Prev Frame Position Script
   3 Numericpad7 mb Nudge to Next Frame Position Script  
   1 Numericpad1 mb Nudge Key and Key Smooth Up Script
   3 Numericpad1 mb Nudge Key and Key Smooth Down Script
```
