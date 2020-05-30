# Aviewer

Simple GUI for watching anime from gogoanime with mpv.

## Installation/Running
### Linux

You need to have mpv installed and usable in your $PATH.
After mpv is installed, run following commands in the folder where you placed the binary:
`chmod +x <name of the binary>`
`./<name of the binary>`

### Windows 

Mpv comes bundled in the zip, but you can use your own as long as it's named <b>mpv.exe</b>.
Run the <b>GUI.exe</b> by double clicking.

## Running from source

If you want to run from source in windows use the psg-win branch.
Following dependecies are required in order to run from source:

 - pysimplegui
 - beautifulsoup4
 - requests
 - lxml

Both scripts need to be in the same folder,
and the script has to be ran from the project's root.
