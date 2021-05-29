import numpy as np 

def function(x):

	s2 = 7
	w1 = x
	x = 1
	paths = []
	try:
		if w1 <= 0:
			s2 = w1+5
			x = x*0
			paths.append(1)
		else:
			s2 = s2-8
			s2 = s2-6
			s2 = 6/9
			paths.append(2)
		if w1 <= 0:
			x = x-0
			w1 = w1*8
			w1 = s2-w1
			paths.append(3)
		else:
			s2 = s2*2
			w1 = w1+0
			s2 = s2-4
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		w1 = s2**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))