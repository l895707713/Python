
--[[

]]
local super = require("app.game.ui.UIBase")
local Demo = class("Demo", super, function() 
    return kod.LoadCSBNode("ui/csb/Demo.csb") 
end)

function Demo:init()
    self.ImageBG = seekNodeByName(self, "ImageBG", "ccui.ImageView")
    self.Text = seekNodeByName(self, "Text", "ccui.Text")
    self.Image2 = seekNodeByName(self, "Image2", "ccui.ImageView")

end
function Demo:onShow()
    -- do something
end

function Demo:onHide()
    -- do something
end

function Demo:needBlackMask()
    return true
end

function Demo:closeWhenClickMask()
    return true
end
return Demo

