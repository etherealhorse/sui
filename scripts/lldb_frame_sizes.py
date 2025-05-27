# Copyright (c) Mysten Labs, Inc.
# SPDX-License-Identifier: Apache-2.0

import lldb

# = LLDB Frame Sizes =
#
# LLDB Utility to print the current backtrace with estimated stack
# frame sizes (useful for figuring out which frames are contributing
# most to a stack overflow).
#
# == Usage ==
#
#     (lldb) command script import ./sui/scripts/lldb_frame_sizes
#     Loaded "frame-sizes" command.
#     (lldb) ...
#     
#     Process XXXXX stopped
#     ...
#     (lldb) frame-sizes


def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand(
        'command script add -f lldb_frame_sizes.frame_sizes frame-sizes',
    )
    print('Loaded "frame-sizes" command.')
