import sublime, sublime_plugin
import os

# Command "Send To SandBox"
class SendSelection( sublime_plugin.WindowCommand ):

   def run(self):
      sSettings = sublime.load_settings('SendToSandbox.sublime-settings')

      sSel = self.window.active_view().sel()
      for region in sSel:
         firstLine = self.window.active_view().rowcol(region.a)
         lastLine = self.window.active_view().rowcol(region.b)

         if (lastLine[0] < firstLine[0] ):
            firstLine = lastLine
            lastLine  = self.window.active_view().rowcol(region.a)


         szText = self.window.active_view().substr(region)
      
         fSandBox = sSettings.get("file")

         if not fSandBox:
            return False

         filePath = self.window.active_view().file_name();

         with open(fSandBox, "a") as myfile:
             myfile.write("\n")
             filePath = ("## %s - [%i-%i]\n" % (filePath, firstLine[0]+1, lastLine[0]+1) )
             myfile.write( filePath)
             myfile.write( szText )
             myfile.write("\n")
 
   def is_enabled(self):
      # Mostro solo se la selezione non è vuota
      sSel = self.window.active_view().sel()
      for region in sSel: 
         szText = self.window.active_view().substr(region)
         szText = szText.strip()
         if szText:
            return True

      return False

