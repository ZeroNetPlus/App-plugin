from Plugin import PluginManager
from Translate import Translate
from cStringIO import StringIO
from Config import config


if "_" not in locals():
    _ = Translate("plugins/UiConfig/languages/")

    def actionUiMedia(self, path, *args, **kwargs):
        if path.startswith("/uimedia/plugins/app/"):
            file_path = path.replace("/uimedia/plugins/app/", "plugins/App/media/")
            if config.debug and (file_path.endswith("all.js") or file_path.endswith("all.css")):
                # If debugging merge *.css to all.css and *.js to all.js
                from Debug import DebugMedia
                DebugMedia.merge(file_path)

            if file_path.endswith("js"):
                data = _.translateData(open(file_path).read(), mode="js")
            elif file_path.endswith("html"):
                data = _.translateData(open(file_path).read(), mode="html")
            else:
                data = open(file_path).read()

            return self.actionFile(file_path, file_obj=StringIO(data), file_size=len(data))
        else:
            return super(UiRequestPlugin, self).actionUiMedia(path)

