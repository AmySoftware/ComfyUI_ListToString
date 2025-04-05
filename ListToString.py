class ListToString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_list": ("STRING", {"multiline": False, "forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_string",)
    FUNCTION = "convert"
    CATEGORY = "Utils"

    def convert(self, input_list):
        if isinstance(input_list, list) and input_list:
            return (input_list[0],)  # Return the first item as a single string
        return ("",)  # Return empty string if input is invalid or empty

# Define the required mappings for ComfyUI to register the node
NODE_CLASS_MAPPINGS = {
    "ListToString": ListToString
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ListToString": "List to String"
}