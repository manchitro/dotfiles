---@type ChadrcConfig
local M = {}

M.ui = { theme = 'catppuccin' }
M.plugins = 'custom.plugins'
M.mappings = require "custom.mappings"

vim.opt.tabstop = 4 -- Number of spaces tabs count for
vim.opt.shiftwidth = 4 -- Number of spaces to use for autoindent
vim.opt.expandtab = true -- Use spaces instead of tabs

vim.opt.ignorecase = true -- Case insensitive searching
vim.opt.smartcase = true -- Case-sensitive if expresson contains a capital letter

vim.opt.scrolloff = 999 -- Keep cursor centered

vim.opt.guicursor = 'n-v-c-sm:block,i-ci-ve:ver25-blinkon200,r-cr-o:hor20' -- blinking cursor in insert mode

-- vim.opt.hlsearch = true -- Highlight search results

return M
