local plugins = {
  {"mhinz/vim-startify",                lazy=false},
  {"xiyaowong/transparent.nvim",        lazy=false},
  {"lambdalisue/suda.vim",              lazy=false},
  {"Exafunction/codeium.vim",           lazy=false},
  {"qpkorr/vim-renamer",                lazy=false},
  {"christoomey/vim-tmux-navigator",    lazy=false},
  {"cwfoo/vim-text-omnicomplete",       lazy=false},
  {"rmagatti/auto-session",
      config = function()
    require("auto-session").setup {
      log_level = "error",
      auto_session_suppress_dirs = { "~/", "~/Projects", "~/Downloads", "/"},
    }
  end
    },
  {"kylechui/nvim-surround",
     version = "*", -- Use for stability; omit to use `main` branch for the latest features
     event = "VeryLazy",
     config = function()
         require("nvim-surround").setup({
             -- Configuration here, or leave empty to use defaults
         })
     end }
}
return plugins

