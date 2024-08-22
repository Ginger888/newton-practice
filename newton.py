{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "94f2b529-d0a7-4d7b-b1ce-7d3b3f32912d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-0.5984681383797152\n",
      "3.2470121395045255\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "def drvt(f,x):\n",
    "    eps = 0.00001\n",
    "    print((f(x+eps)-f(x))/eps)\n",
    "    return (f(x+eps)-f(x))/eps\n",
    "\n",
    "def drvt2(f,x):\n",
    "    eps = 0.00001\n",
    "    f2= ((f(x+eps*2)-f(x+eps))/eps - (f(x+eps)-f(x))/eps)/eps\n",
    "    return f2\n",
    "x = 2.5\n",
    "f = np.cos\n",
    "eps = 1\n",
    "while eps > 0.0000001:\n",
    "    eps = drvt(f,x)/drvt2(f,x)\n",
    "    x = x- eps\n",
    "    \n",
    "\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd1c3689-bfe2-4aba-8bee-ad24eec5fa38",
   "metadata": {},
   "outputs": [],
   "source": [
    "git clone https://github.com/<ginger888>/newton-practice"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
