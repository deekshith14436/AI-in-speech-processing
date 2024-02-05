#!/usr/bin/env python
# coding: utf-8

# In[1]:


# M Deekshith Reddy
#bl.en.u4aie21081
pip install librosa


# In[10]:


import librosa

y, sr = librosa.load("voice1.wav")
librosa.display.waveshow(y)


# In[11]:


import numpy as np
print("Length of the  voice signal:",len(y),"samples")
print("Magnitude range of the signal :",np.min(y),"to", np.max(y))
print("Sampling rate of the signal:",sr, "Hz")


# In[15]:


import IPython.display as ipd

start = int(0.5 * sr)
end = int(2 * sr)
segments = y[start:end]
librosa.display.waveshow(segments)
ipd.Audio(segments, rate=sr)


# In[26]:


from matplotlib import pyplot as plt
segment_1_start = int(0 * sr)
segment_1_end = int(2 * sr)
segment_2_start = int(0.8 * sr)
segment_2_end = int(3 * sr)
segment_3_start = int(1.4 * sr)
segment_3_end = int(2.5 * sr)
segment_1 = y[segment_1_start:segment_1_end]
segment_2 = y[segment_2_start:segment_2_end]
segment_3 = y[segment_3_start:segment_3_end]
print("Playing Segment 1:")

plt.figure(figsize=(10, 5))
librosa.display.waveshow(segment_1, color = 'orange')
plt.title('Segment-1')
plt.show()
ipd.Audio(segment_1, rate=sr)
print("Playing Segment 2:")

plt.figure(figsize=(10, 5))
librosa.display.waveshow(segment_2, color = 'green')
plt.title('Segment-2')
plt.show()
ipd.Audio(segment_2, rate=sr)

plt.figure(figsize=(10, 5))
librosa.display.waveshow(segment_3, color = 'black')
plt.title('Segment-3')
plt.show()
ipd.Audio(segment_3, rate=sr)


# In[ ]:




