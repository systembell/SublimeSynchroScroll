import sublime, sublime_plugin

class SynchroScrollCommand(sublime_plugin.WindowCommand):
   def run(self, cmd="", **kwargs):
      if cmd:
         grpcount = self.window.num_groups()
         if grpcount > 1:
            for grp in range(grpcount):
               synchroscroll = self.window.active_view_in_group(grp)
               if synchroscroll:
                   synchroscroll.run_command(cmd, kwargs)