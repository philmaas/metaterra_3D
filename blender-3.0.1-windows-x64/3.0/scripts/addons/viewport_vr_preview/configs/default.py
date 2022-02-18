actionconfig_version = (3, 0, 39)
actionconfig_data = \
[("blender_default",
  {"items":
   [("controller_grip", {"type": 'POSE', "user_path0": '/user/hand/left', "user_path1": '/user/hand/right', "pose_is_controller_grip": 'True', "pose_is_controller_aim": 'False'}, None,
     {"bindings":
      [("cosmos", {"profile": '/interaction_profiles/htc/vive_cosmos_controller', "component_path0": '/input/grip/pose', "component_path1": '/input/grip/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ("huawei", {"profile": '/interaction_profiles/huawei/controller', "component_path0": '/input/grip/pose', "component_path1": '/input/grip/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ("index", {"profile": '/interaction_profiles/valve/index_controller', "component_path0": '/input/grip/pose', "component_path1": '/input/grip/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ("oculus", {"profile": '/interaction_profiles/oculus/touch_controller', "component_path0": '/input/grip/pose', "component_path1": '/input/grip/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ("reverb_g2", {"profile": '/interaction_profiles/hp/mixed_reality_controller', "component_path0": '/input/grip/pose', "component_path1": '/input/grip/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ("simple", {"profile": '/interaction_profiles/khr/simple_controller', "component_path0": '/input/grip/pose', "component_path1": '/input/grip/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ("vive", {"profile": '/interaction_profiles/htc/vive_controller', "component_path0": '/input/grip/pose', "component_path1": '/input/grip/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ("wmr", {"profile": '/interaction_profiles/microsoft/motion_controller', "component_path0": '/input/grip/pose', "component_path1": '/input/grip/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ],
      },
     ),
    ("controller_aim", {"type": 'POSE', "user_path0": '/user/hand/left', "user_path1": '/user/hand/right', "pose_is_controller_grip": 'False', "pose_is_controller_aim": 'True'}, None,
     {"bindings":
      [("cosmos", {"profile": '/interaction_profiles/htc/vive_cosmos_controller', "component_path0": '/input/aim/pose', "component_path1": '/input/aim/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ("huawei", {"profile": '/interaction_profiles/huawei/controller', "component_path0": '/input/aim/pose', "component_path1": '/input/aim/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ("index", {"profile": '/interaction_profiles/valve/index_controller', "component_path0": '/input/aim/pose', "component_path1": '/input/aim/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ("oculus", {"profile": '/interaction_profiles/oculus/touch_controller', "component_path0": '/input/aim/pose', "component_path1": '/input/aim/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ("reverb_g2", {"profile": '/interaction_profiles/hp/mixed_reality_controller', "component_path0": '/input/aim/pose', "component_path1": '/input/aim/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ("simple", {"profile": '/interaction_profiles/khr/simple_controller', "component_path0": '/input/aim/pose', "component_path1": '/input/aim/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ("vive", {"profile": '/interaction_profiles/htc/vive_controller', "component_path0": '/input/aim/pose', "component_path1": '/input/aim/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ("wmr", {"profile": '/interaction_profiles/microsoft/motion_controller', "component_path0": '/input/aim/pose', "component_path1": '/input/aim/pose', "pose_location": '(0.0, 0.0, 0.0)', "pose_rotation": '(0.0, 0.0, 0.0)'}),
       ],
      },
     ),
    ("teleport", {"type": 'FLOAT', "user_path0": '/user/hand/left', "user_path1": '/user/hand/right', "op": 'wm.xr_navigation_teleport', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("interpolation", 0.9),
       ("color", (0.0, 1.0, 1.0, 1.0)),
       ],
      },
     {"bindings":
      [("cosmos", {"profile": '/interaction_profiles/htc/vive_cosmos_controller', "component_path0": '/input/trigger/value', "component_path1": '/input/trigger/value', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("huawei", {"profile": '/interaction_profiles/huawei/controller', "component_path0": '/input/trigger/value', "component_path1": '/input/trigger/value', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("index", {"profile": '/interaction_profiles/valve/index_controller', "component_path0": '/input/trigger/value', "component_path1": '/input/trigger/value', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("oculus", {"profile": '/interaction_profiles/oculus/touch_controller', "component_path0": '/input/trigger/value', "component_path1": '/input/trigger/value', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("reverb_g2", {"profile": '/interaction_profiles/hp/mixed_reality_controller', "component_path0": '/input/trigger/value', "component_path1": '/input/trigger/value', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("simple", {"profile": '/interaction_profiles/khr/simple_controller', "component_path0": '/input/select/click', "component_path1": '/input/select/click', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("vive", {"profile": '/interaction_profiles/htc/vive_controller', "component_path0": '/input/trigger/value', "component_path1": '/input/trigger/value', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("wmr", {"profile": '/interaction_profiles/microsoft/motion_controller', "component_path0": '/input/trigger/value', "component_path1": '/input/trigger/value', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ],
      },
     ),
    ("nav_grab", {"type": 'FLOAT', "user_path0": '/user/hand/left', "user_path1": '/user/hand/right', "op": 'wm.xr_navigation_grab', "op_mode": 'MODAL', "bimanual": 'True', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("lock_rotation", True),
       ],
      },
     {"bindings":
      [("cosmos", {"profile": '/interaction_profiles/htc/vive_cosmos_controller', "component_path0": '/input/squeeze/click', "component_path1": '/input/squeeze/click', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("huawei", {"profile": '/interaction_profiles/huawei/controller', "component_path0": '/input/trackpad/click', "component_path1": '/input/trackpad/click', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("index", {"profile": '/interaction_profiles/valve/index_controller', "component_path0": '/input/squeeze/force', "component_path1": '/input/squeeze/force', "threshold": '0.5', "axis_region": 'ANY'}),
       ("oculus", {"profile": '/interaction_profiles/oculus/touch_controller', "component_path0": '/input/squeeze/value', "component_path1": '/input/squeeze/value', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("reverb_g2", {"profile": '/interaction_profiles/hp/mixed_reality_controller', "component_path0": '/input/squeeze/value', "component_path1": '/input/squeeze/value', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("simple", {"profile": '/interaction_profiles/khr/simple_controller', "component_path0": '/input/menu/click', "component_path1": '/input/menu/click', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("vive", {"profile": '/interaction_profiles/htc/vive_controller', "component_path0": '/input/squeeze/click', "component_path1": '/input/squeeze/click', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("wmr", {"profile": '/interaction_profiles/microsoft/motion_controller', "component_path0": '/input/squeeze/click', "component_path1": '/input/squeeze/click', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ],
      },
     ),
    ("fly_forward", {"type": 'FLOAT', "user_path0": '/user/hand/left', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'VIEWER_FORWARD'),
       ("lock_location_z", True),
       ],
      }, 
     {"bindings":
      [("cosmos", {"profile": '/interaction_profiles/htc/vive_cosmos_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("huawei", {"profile": '/interaction_profiles/huawei/controller', "component_path0": '/input/trackpad/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("index", {"profile": '/interaction_profiles/valve/index_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("oculus", {"profile": '/interaction_profiles/oculus/touch_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("reverb_g2", {"profile": '/interaction_profiles/hp/mixed_reality_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("vive", {"profile": '/interaction_profiles/htc/vive_controller', "component_path0": '/input/trackpad/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("wmr", {"profile": '/interaction_profiles/microsoft/motion_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ],
      },
     ),
    ("fly_back", {"type": 'FLOAT', "user_path0": '/user/hand/left', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'VIEWER_BACK'),
       ("lock_location_z", True),
       ],
      },  
     {"bindings":
      [("cosmos", {"profile": '/interaction_profiles/htc/vive_cosmos_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("huawei", {"profile": '/interaction_profiles/huawei/controller', "component_path0": '/input/trackpad/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("index", {"profile": '/interaction_profiles/valve/index_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("oculus", {"profile": '/interaction_profiles/oculus/touch_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("reverb_g2", {"profile": '/interaction_profiles/hp/mixed_reality_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("vive", {"profile": '/interaction_profiles/htc/vive_controller', "component_path0": '/input/trackpad/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("wmr", {"profile": '/interaction_profiles/microsoft/motion_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ],
      },
     ),
    ("fly_left", {"type": 'FLOAT', "user_path0": '/user/hand/left', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'VIEWER_LEFT'),
       ("lock_location_z", True),
       ],
      }, 
     {"bindings":
      [("cosmos", {"profile": '/interaction_profiles/htc/vive_cosmos_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("huawei", {"profile": '/interaction_profiles/huawei/controller', "component_path0": '/input/trackpad/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("index", {"profile": '/interaction_profiles/valve/index_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("oculus", {"profile": '/interaction_profiles/oculus/touch_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("reverb_g2", {"profile": '/interaction_profiles/hp/mixed_reality_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("vive", {"profile": '/interaction_profiles/htc/vive_controller', "component_path0": '/input/trackpad/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("wmr", {"profile": '/interaction_profiles/microsoft/motion_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ],
      },
     ),
    ("fly_right", {"type": 'FLOAT', "user_path0": '/user/hand/left', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'VIEWER_RIGHT'),
       ("lock_location_z", True),
       ],
      },   
     {"bindings":
      [("cosmos", {"profile": '/interaction_profiles/htc/vive_cosmos_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("huawei", {"profile": '/interaction_profiles/huawei/controller', "component_path0": '/input/trackpad/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("index", {"profile": '/interaction_profiles/valve/index_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("oculus", {"profile": '/interaction_profiles/oculus/touch_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("reverb_g2", {"profile": '/interaction_profiles/hp/mixed_reality_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("vive", {"profile": '/interaction_profiles/htc/vive_controller', "component_path0": '/input/trackpad/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("wmr", {"profile": '/interaction_profiles/microsoft/motion_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ],
      },
     ),
    ("fly_up", {"type": 'FLOAT', "user_path0": '/user/hand/right', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'UP'),
       ("speed_min", 0.014),
       ("speed_max", 0.042),
       ],
      }, 
     {"bindings":
      [("cosmos", {"profile": '/interaction_profiles/htc/vive_cosmos_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("huawei", {"profile": '/interaction_profiles/huawei/controller', "component_path0": '/input/trackpad/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("index", {"profile": '/interaction_profiles/valve/index_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("oculus", {"profile": '/interaction_profiles/oculus/touch_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("reverb_g2", {"profile": '/interaction_profiles/hp/mixed_reality_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("vive", {"profile": '/interaction_profiles/htc/vive_controller', "component_path0": '/input/trackpad/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("wmr", {"profile": '/interaction_profiles/microsoft/motion_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ],
      },
     ),
    ("fly_down", {"type": 'FLOAT', "user_path0": '/user/hand/right', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'DOWN'),
       ("speed_min", 0.014),
       ("speed_max", 0.042),
       ],
      },  
     {"bindings":
      [("cosmos", {"profile": '/interaction_profiles/htc/vive_cosmos_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("huawei", {"profile": '/interaction_profiles/huawei/controller', "component_path0": '/input/trackpad/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("index", {"profile": '/interaction_profiles/valve/index_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("oculus", {"profile": '/interaction_profiles/oculus/touch_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("reverb_g2", {"profile": '/interaction_profiles/hp/mixed_reality_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("vive", {"profile": '/interaction_profiles/htc/vive_controller', "component_path0": '/input/trackpad/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("wmr", {"profile": '/interaction_profiles/microsoft/motion_controller', "component_path0": '/input/thumbstick/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ],
      },
     ),
    ("fly_turnleft", {"type": 'FLOAT', "user_path0": '/user/hand/right', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'TURNLEFT'),
       ("speed_min", 0.01),
       ("speed_max", 0.03),
       ],
      },
     {"bindings":
      [("cosmos", {"profile": '/interaction_profiles/htc/vive_cosmos_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("huawei", {"profile": '/interaction_profiles/huawei/controller', "component_path0": '/input/trackpad/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("index", {"profile": '/interaction_profiles/valve/index_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("oculus", {"profile": '/interaction_profiles/oculus/touch_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("reverb_g2", {"profile": '/interaction_profiles/hp/mixed_reality_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("vive", {"profile": '/interaction_profiles/htc/vive_controller', "component_path0": '/input/trackpad/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ("wmr", {"profile": '/interaction_profiles/microsoft/motion_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ],
      },
     ),
    ("fly_turnright", {"type": 'FLOAT', "user_path0": '/user/hand/right', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'TURNRIGHT'),
       ("speed_min", 0.01),
       ("speed_max", 0.03),
       ],
      },  
     {"bindings":
      [("cosmos", {"profile": '/interaction_profiles/htc/vive_cosmos_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("huawei", {"profile": '/interaction_profiles/huawei/controller', "component_path0": '/input/trackpad/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("index", {"profile": '/interaction_profiles/valve/index_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("oculus", {"profile": '/interaction_profiles/oculus/touch_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("reverb_g2", {"profile": '/interaction_profiles/hp/mixed_reality_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("vive", {"profile": '/interaction_profiles/htc/vive_controller', "component_path0": '/input/trackpad/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ("wmr", {"profile": '/interaction_profiles/microsoft/motion_controller', "component_path0": '/input/thumbstick/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ],
      },
     ),
    ("nav_reset", {"type": 'FLOAT', "user_path0": '/user/hand/left', "user_path1": '/user/hand/right', "op": 'wm.xr_navigation_reset', "op_mode": 'PRESS', "bimanual": 'False', "haptic_name": 'haptic', "haptic_match_user_paths": 'True', "haptic_duration": '0.30000001192092896', "haptic_frequency": '3000.0', "haptic_amplitude": '0.5', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("location", False),
       ("rotation", False),
       ("scale", True),
       ],
      }, 
     {"bindings":
      [("cosmos", {"profile": '/interaction_profiles/htc/vive_cosmos_controller', "component_path0": '/input/x/click', "component_path1": '/input/a/click', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("huawei", {"profile": '/interaction_profiles/huawei/controller', "component_path0": '/input/back/click', "component_path1": '/input/back/click', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("index", {"profile": '/interaction_profiles/valve/index_controller', "component_path0": '/input/a/click', "component_path1": '/input/a/click', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("oculus", {"profile": '/interaction_profiles/oculus/touch_controller', "component_path0": '/input/x/click', "component_path1": '/input/a/click', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("reverb_g2", {"profile": '/interaction_profiles/hp/mixed_reality_controller', "component_path0": '/input/x/click', "component_path1": '/input/a/click', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("vive", {"profile": '/interaction_profiles/htc/vive_controller', "component_path0": '/input/menu/click', "component_path1": '/input/menu/click', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ("wmr", {"profile": '/interaction_profiles/microsoft/motion_controller', "component_path0": '/input/menu/click', "component_path1": '/input/menu/click', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ],
      },
     ),
    ("haptic", {"type": 'VIBRATION', "user_path0": '/user/hand/left', "user_path1": '/user/hand/right'}, None,
     {"bindings":
      [("cosmos", {"profile": '/interaction_profiles/htc/vive_cosmos_controller', "component_path0": '/output/haptic', "component_path1": '/output/haptic'}),
       ("huawei", {"profile": '/interaction_profiles/huawei/controller', "component_path0": '/output/haptic', "component_path1": '/output/haptic'}),
       ("index", {"profile": '/interaction_profiles/valve/index_controller', "component_path0": '/output/haptic', "component_path1": '/output/haptic'}),
       ("oculus", {"profile": '/interaction_profiles/oculus/touch_controller', "component_path0": '/output/haptic', "component_path1": '/output/haptic'}),
       ("reverb_g2", {"profile": '/interaction_profiles/hp/mixed_reality_controller', "component_path0": '/output/haptic', "component_path1": '/output/haptic'}),
       ("simple", {"profile": '/interaction_profiles/khr/simple_controller', "component_path0": '/output/haptic', "component_path1": '/output/haptic'}),
       ("vive", {"profile": '/interaction_profiles/htc/vive_controller', "component_path0": '/output/haptic', "component_path1": '/output/haptic'}),
       ("wmr", {"profile": '/interaction_profiles/microsoft/motion_controller', "component_path0": '/output/haptic', "component_path1": '/output/haptic'}),
       ],
      },
     ),
    ],
   },
  ),
 ("blender_default_gamepad",
  {"items":
   [("teleport", {"type": 'FLOAT', "user_path0": '/user/gamepad', "user_path1": '', "op": 'wm.xr_navigation_teleport', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("interpolation", 0.9),
       ("from_viewer", True),
       ("color", (0.0, 1.0, 1.0, 1.0)),
       ],
      }, 
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/input/trigger_right/value', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ],
      },
     ),
    ("fly", {"type": 'FLOAT', "user_path0": '/user/gamepad', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'}, None,
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/input/trigger_left/value', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ],
      },
     ),
    ("fly_forward", {"type": 'FLOAT', "user_path0": '/user/gamepad', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'VIEWER_FORWARD'),
       ("lock_location_z", True),
       ],
      }, 
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/input/thumbstick_left/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ],
      },
     ),
    ("fly_back", {"type": 'FLOAT', "user_path0": '/user/gamepad', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'VIEWER_BACK'),
       ("lock_location_z", True),
       ],
      },  
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/input/thumbstick_left/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ],
      },
     ),
    ("fly_left", {"type": 'FLOAT', "user_path0": '/user/gamepad', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'VIEWER_LEFT'),
       ("lock_location_z", True),
       ],
      }, 
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/input/thumbstick_left/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ],
      },
     ),
    ("fly_right", {"type": 'FLOAT', "user_path0": '/user/gamepad', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'VIEWER_RIGHT'),
       ("lock_location_z", True),
       ],
      }, 
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/input/thumbstick_left/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ],
      },
     ),
    ("fly_up", {"type": 'FLOAT', "user_path0": '/user/gamepad', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'UP'),
       ("speed_min", 0.014),
       ("speed_max", 0.042),
       ],
      },   
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/input/thumbstick_right/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ],
      },
     ),
    ("fly_down", {"type": 'FLOAT', "user_path0": '/user/gamepad', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'DOWN'),
       ("speed_min", 0.014),
       ("speed_max", 0.042),
       ],
      },   
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/input/thumbstick_right/y', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ],
      },
     ),
    ("fly_turnleft", {"type": 'FLOAT', "user_path0": '/user/gamepad', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'TURNLEFT'),
       ("speed_min", 0.01),
       ("speed_max", 0.03),
       ],
      },  
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/input/thumbstick_right/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'NEGATIVE'}),
       ],
      },
     ),
    ("fly_turnright", {"type": 'FLOAT', "user_path0": '/user/gamepad', "user_path1": '', "op": 'wm.xr_navigation_fly', "op_mode": 'MODAL', "bimanual": 'False', "haptic_name": '', "haptic_match_user_paths": 'False', "haptic_duration": '0.0', "haptic_frequency": '0.0', "haptic_amplitude": '0.0', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("mode", 'TURNRIGHT'),
       ("speed_min", 0.01),
       ("speed_max", 0.03),
       ],
      }, 
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/input/thumbstick_right/x', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'POSITIVE'}),
       ],
      },
     ),
    ("nav_reset", {"type": 'FLOAT', "user_path0": '/user/gamepad', "user_path1": '', "op": 'wm.xr_navigation_reset', "op_mode": 'PRESS', "bimanual": 'False', "haptic_name": 'haptic_right', "haptic_match_user_paths": 'True', "haptic_duration": '0.30000001192092896', "haptic_frequency": '3000.0', "haptic_amplitude": '0.5', "haptic_mode": 'PRESS'},
     {"op_properties":
      [("location", False),
       ("rotation", False),
       ("scale", True),
       ],
      },  
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/input/a/click', "component_path1": '', "threshold": '0.30000001192092896', "axis_region": 'ANY'}),
       ],
      },
     ),
    ("haptic_left", {"type": 'VIBRATION', "user_path0": '/user/gamepad', "user_path1": ''}, None,
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/output/haptic_left', "component_path1": ''}),
       ],
      },
     ),
    ("haptic_right", {"type": 'VIBRATION', "user_path0": '/user/gamepad', "user_path1": ''}, None,
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/output/haptic_right', "component_path1": ''}),
       ],
      },
     ),
    ("haptic_lefttrigger", {"type": 'VIBRATION', "user_path0": '/user/gamepad', "user_path1": ''}, None,
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/output/haptic_left_trigger', "component_path1": ''}),
       ],
      },
     ),
    ("haptic_righttrigger", {"type": 'VIBRATION', "user_path0": '/user/gamepad', "user_path1": ''}, None,
     {"bindings":
      [("gamepad", {"profile": '/interaction_profiles/microsoft/xbox_controller', "component_path0": '/output/haptic_right_trigger', "component_path1": ''}),
       ],
      },
     ),
    ],
   },
  ),
 ]


if __name__ == "__main__":
    # Only add keywords that are supported.
    from bpy.app import version as blender_version
    keywords = {}
    if blender_version >= (3, 0, 0):
        keywords["actionconfig_version"] = actionconfig_version
    import os
    from viewport_vr_preview.io import actionconfig_import_from_data
    actionconfig_import_from_data(
        os.path.splitext(os.path.basename(__file__))[0],
        actionconfig_data,
        **keywords,
    )