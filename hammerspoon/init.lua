--[[
Hammerspoon configuration file
--]]

-- Hello, world!
hs.hotkey.bind({"cmd", "alt", "ctrl"}, "W", function()
    -- Heads-up display notification
    hs.alert.show("Hello, Hammerspoon world!")
end)
