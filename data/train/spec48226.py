import numpy as np 

def function(x):

	k9 = 1
	w1 = x
	paths = []
	try:
		if w1 < 1:
			k9 = 0*k9
			paths.append(1)
		else:
			x = x*w1
			w1 = k9*w1
			paths.append(2)
		if w1 > 7:
			w1 = 3/x
			x = x*0
			paths.append(3)
		else:
			w1 = x*2
			w1 = w1+6
			x = 5*k9
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		w1 = w1**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))