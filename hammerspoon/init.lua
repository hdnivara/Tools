--[[
Hammerspoon configuration file
--]]

-- Hotkeys
local mash = {"cmd", "alt", "ctrl"}

-- Hello, world!
hs.hotkey.bind(mash, "W", function()
    -- Heads-up display notification
    hs.alert.show("Hello, Hammerspoon world!")

    -- Mac OS X style notification
    hs.notify.new({title="Hammerspoon",
        informativeText="Hello, Hammerspoon world!"}):send()
end)
