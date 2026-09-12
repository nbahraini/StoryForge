"""سرویس اتصال به ComfyUI"""
import requests
import json
import time
from config import COMFYUI_CONFIG

class ComfyUIService:
    def __init__(self):
        self.host = COMFYUI_CONFIG["host"]
    
    def queue_prompt(self, prompt_data):
        """ارسال درخواست تولید تصویر"""
        try:
            response = requests.post(
                f"{self.host}/prompt",
                json={"prompt": prompt_data}
            )
            return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    def get_image(self, prompt_text, negative_prompt="", steps=20, cfg=7):
        """تولید تصویر از متن"""
        workflow = {
            "3": {
                "class_type": "KSampler",
                "inputs": {
                    "seed": -1,
                    "steps": steps,
                    "cfg": cfg,
                    "sampler_name": "euler",
                    "scheduler": "normal",
                    "denoise": 1
                }
            },
            "4": {
                "class_type": "CheckpointLoaderSimple",
                "inputs": {"ckpt_name": "sd_xl_base_1.0.safetensors"}
            },
            "5": {
                "class_type": "CLIPTextEncode",
                "inputs": {"text": prompt_text, "clip": ["4", 1]}
            },
            "6": {
                "class_type": "CLIPTextEncode",
                "inputs": {"text": negative_prompt, "clip": ["4", 1]}
            },
            "7": {
                "class_type": "SaveImage",
                "inputs": {"filename_prefix": "character", "images": ["3", 0]}
            }
        }
        
        workflow["3"]["inputs"]["model"] = ["4", 0]
        workflow["3"]["inputs"]["positive"] = ["5", 0]
        workflow["3"]["inputs"]["negative"] = ["6", 0]
        
        return self.queue_prompt(workflow)
    
    def check_connection(self):
        """بررسی اتصال به ComfyUI"""
        try:
            response = requests.get(f"{self.host}/system_stats", timeout=5)
            return response.status_code == 200
        except:
            return False

# Singleton instance
comfyui_service = ComfyUIService()