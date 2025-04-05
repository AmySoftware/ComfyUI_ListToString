# ComfyUI_ListToString
[ComfyUI](https://github.com/comfyanonymous/ComfyUI/) node to convert from List to String.

I had problem with [ComfyUI-IF_LLM](https://github.com/if-ai/ComfyUI-IF_LLM) response output so I made this converter.

## **Installation**
Copy ListToString.py and put it in ComfyUI/custom_nodes/

## **Usage**
1. Add node -> Utils -> ListToString
2. Connect ComfyUI-IF_LLM response node to this node's text input, then connect the text output to any text input node (Clip Text Encoder, Text Combine/Concat etc).
