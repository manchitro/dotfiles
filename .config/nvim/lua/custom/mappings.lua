local M = {}

-- In order to disable a default keymap, use
M.disabled = {
    n = {
        ["<leader>h"] = "",
        ["<C-a>"] = ""
    }
}

-- Your custom mappings
M.abc = {
    n = {
        ["<C-n>"] = {"<cmd> Telescope <CR>", "Telescope"},
        ["H"] = {"^", "beginning of line"},
        ["L"] = {"$", "end of line"},
        ["<C-s>"] = {":w <CR>", "save file"},
        ["<A-z>"] = {":set wrap!<CR>", "toggle wrap"},
    },

    i = {
        ["kj"] = { "<ESC>", "escape insert mode" , opts = { nowait = true }},
        ["<C-s>"] = {":w <CR>", "save file"},
    },

    v = {
        ["<C-c>"] = {"\"*y :let @+=@*<CR>", "copy to clipboard"},
        ["H"] = {"^", "beginning of line"},
        ["L"] = {"$", "end of line"},
        ["<C-s>"] = {":w <CR>", "save file"},
    }
}

return M
