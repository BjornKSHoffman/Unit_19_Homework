{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'os' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-98c2a65eeaba>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mmnemonic\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgetenv\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'MNEMONIC'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'diamond session puzzle siege jewel spell melt pen index torch liberty sniff'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'os' is not defined"
     ]
    }
   ],
   "source": [
    "mnemonic = os.getenv('MNEMONIC', 'diamond session puzzle siege jewel spell melt pen index torch liberty sniff')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
