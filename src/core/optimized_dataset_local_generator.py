# # Claude Sonnet Recommendation

# class OptimizedQAGenerator:
#     def __init__(self, model='llama3.2:1b', max_workers=2, gpu_threshold=85):
#         self.model = model
#         self.max_workers = max_workers
#         self.gpu_threshold = gpu_threshold
#         self.processing_times = []


#     def monitor_gpu_usage(self):
#         """Monitor GPU usage and return current utilization"""
#         try:
#              import GPUtil
#              gpus = GPUtil.getGPUs()
#              if gpus:
#                  return gpus[0].load * 100
#         except:
#             pass
#         return 0
    
#     def local_model_generate_optimized(self, text_chunk, retry_count=3):
#         """Optimized version with error handling and monitoring"""
#         prompt = f"""
#         You are an assistant that creates educational datasets.
#         Given the following text, generate:
#         1. A clear and consise question about the content.
#         2. A correct answer to that question.
#         3. A detailed explanation of why that answer is correct.

#         Text:
#         {text_chunk}

#         Respond ONLY in Valid JSON format as:
#         {{
#             "question": "...",
#             "answer": "...",
#             "explanation": "..."
#         }}
#         """
#         for attempt in range(retry_count):
#             try:
#                 import time
#                 start_time = time.time()
                
#                 from ollama import chat, ChatResponse
#                 response: ChatResponse = chat(
#                     model=self.model,
#                     messages=[{'role': 'user', 'content': prompt}],
#                     options={
#                         'temperature': 0.7,
#                         'top_p': 0.9,
#                         'num_ctx': 1024,  # Reduced context window
#                         'num_predict': 256,  # Limit response length
#                         'num_thread': 4,  # Limit CPU threads
#                     }
#                 )
#                 processing_time = time.time() - start_time
#                 self.processing_times.append(processing_time)
                
#                 output_text = response['message']['content']
#                 import json
#                 qa_data = json.loads(output_text.strip())

#                 return qa_data, processing_time
            
#             except json.JSONDecodeError as ex:
#                 print(f"JSON decode error on attempt {attempt + 1}: {ex}")
#                 if attempt == retry_count - 1:
#                     return None, 0

#             except Exception as e:
#                 print(f"Error on attempt {attempt + 1}: {e}")
#                 if attempt == retry_count - 1:
#                     return None, 0