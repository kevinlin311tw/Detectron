# Copyright (c) 2017-present, Facebook, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################
"""Provide stub objects that can act as stand-in "dummy" datasets for simple use
cases, like getting all classes in a dataset. This exists so that demos can be
run without requiring users to download/install datasets first.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from detectron.utils.collections import AttrDict


def get_coco_dataset():
    """A dummy COCO dataset that includes only the 'classes' field."""
    ds = AttrDict()
    classes = [
        '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
        'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant',
        'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse',
        'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack',
        'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis',
        'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove',
        'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass',
        'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich',
        'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake',
        'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv',
        'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave',
        'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase',
        'scissors', 'teddy bear', 'hair drier', 'toothbrush'
    ]
    ds.classes = {i: name for i, name in enumerate(classes)}
    return ds

def get_ava_dataset():
    """A dummy COCO dataset that includes only the 'classes' field."""
    ds = AttrDict()
    classes = [
        '__background__', 'actor'
    ]
    ds.classes = {i: name for i, name in enumerate(classes)}
    return ds

def get_ava_dataset_action():
    """A dummy COCO dataset that includes only the 'classes' field."""
    ds = AttrDict()
    classes = [
        '__background__', 'bend/bow (at the waist)','crawl', 'crouch/kneel', 'dance', 'fall down', 'get up', 'jump/leap','lie/sleep',
        'martial art','run/jog','sit','stand','swim','walk','answer phone','brush teeth','carry/hold (an object)','catch (an object)',
        'chop','climb (e.g., a mountain)','clink glass','close (e.g., a door, a box)','cook','cut','dig','dress/put on clothing','drink',
        'drive (e.g., a car, a truck)','eat','enter','exit','extract','fishing','hit (an object)','kick (an object)','lift/pick up',
        'listen (e.g., to music)','open (e.g., a window, a car door)','paint','play board game','play musical instrument','play with pets',
        'point to (an object)','press','pull (an object)','push (an object)','put down','read','ride (e.g., a bike, a car, a horse)',
        'row boat','sail boat','shoot','shovel','smoke','stir','take a photo','text on/look at a cellphone','throw','touch (an object)',
        'turn (e.g., a screwdriver)','watch (e.g., TV)','work on a computer','write','fight/hit (a person)','give/serve (an object) to (a person)',
        'grab (a person)','hand clap','hand shake','hand wave','hug (a person)','kick (a person)','kiss (a person)','lift (a person)',
        'listen to (a person)','play with kids','push (another person)','sing to (e.g., self, a person, a group)','take (an object) from (a person)',
        'talk to (e.g., self, a person, a group)','watch (a person)'
    ]
    ds.classes = {i: name for i, name in enumerate(classes)}
    return ds