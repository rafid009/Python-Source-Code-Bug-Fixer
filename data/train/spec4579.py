import numpy as np 

def function(x):

	s1 = 7
	w2 = x
	paths = []
	try:
		if s1 > 9:
			w2 = 6+w2
			w2 = x-6
			s1 = 7-6
			paths.append(1)
		else:
			w2 = 2*2
			s1 = s1+s1
			paths.append(2)
		if s1 <= 3:
			w2 = 6*0
			x = 0-5
			paths.append(3)
		else:
			w2 = s1/w2
			s1 = x*s1
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		x = s1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))