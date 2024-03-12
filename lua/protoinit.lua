-- This is a proof of concept for creating an init file for neovim
-- Intended use is to be used as a vanilla default

local set = vim.opt
local hi = vim.cmd.highlight

set.number = true
set.relativenumber = true
set.autoindent = true
set.tabstop = 4
set.shiftwidth = 4
set.softtabstop = 4
set.termguicolors = true

hi("clear")
vim.cmd [[
	syntax reset
	let g:colors_name = "gnomedark"
	set background=dark
	set t_Co=256
]]
