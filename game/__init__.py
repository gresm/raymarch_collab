# Copyright (c) 2022-NOW holder of an account "gresm" on www.github.com
#
# Licensed under the MIT license: https://opensource.org/licenses/MIT
# Permission is granted to use, copy, modify, and redistribute the work.
# Full license information available in the folder LICENSE file.


from .base_scene import SceneManager, Scene as BaseScene
from .window import *

scene_manager = SceneManager()
del SceneManager
