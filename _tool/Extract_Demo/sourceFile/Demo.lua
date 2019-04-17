local super = require("app.game.ui.UIBase")
local Demo = class("Demo", super, function() 
    return kod.LoadCSBNode("ui/csb/Demo.csb") 
end)

function Demo:init()
    self.ImageBG = seekNodeByName(self, "ImageBG", "ccui.ImageView")
    self.Text = seekNodeByName(self, "Text", "ccui.Text")
    self.Image2 = seekNodeByName(self, "Image2", "ccui.ImageView")

end
function Demo:onShow(goldNum, honerIndex)
    if not goldNum or not honerIndex then 
        print("参数有误，请确认")
        return 
    end 

    local honerName = "徽章：" .. self.getHonerNameByIndex(honerIndex)
    if string.len(honerName) <= 0 then 
        print("没有获取到相关的荣耀徽章名字，其索引为:" .. honerIndex or "nil")
        return 
    end 

    local strContent = string.format("您确定要获取%d的金币和%s的奖励吗？",goldNum, honerName)
    MessageBox:show(strContent)
end

return Demo

