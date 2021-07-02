# Heliostat-Locator
It locates the heliostats, in order to obtain highest efficiency. <a href="https://github.com/Martian-Solar-Power-Plant/Heliostat-Locator/blob/master/Heliostat%20Locator.ipynb" target="_blank">Click here</a> to see how does it work.
<h2>Commands</h2>
<h3>getHL(HG,TP,time)</h3>
It computes the position of the heliostat. It returns the position in <strong>radians</strong>
<br>
<code>HG</code>:Global position of the heliostat(latitude,longitude)
<br>
<code>TP</code>: Position of the tower(azimuth, altitude). Origin of the azimuth is south and all units are in radians
<br>
<code>time</code>: Time of the computed instance. It's a <b>datetime</b> object

<h3>getHL(HG,TP,time)</h3>
It computes the normal of the heliostat. It returns the position in <strong>radians</strong>
<br>
<code>HG</code>:Global position of the heliostat(latitude,longitude)
<br>
<code>TP</code>: Position of the tower(azimuth, altitude). Origin of the azimuth is south and all units are in radians
<br>
<code>time</code>: Time of the computed instance. It's a <b>datetime</b> object
