import numpy as np 

def function(x):

	s1 = x
	w6 = 2
	paths = []
	try:
		if w6 >= 5:
			s1 = 8+5
			s1 = x*1
			s1 = 3/7
			paths.append(1)
		else:
			s1 = s1+w6
			paths.append(2)
		if w6 >= 7:
			s1 = 0+9
			w6 = s1*w6
			w6 = w6+w6
			paths.append(3)
		else:
			s1 = 4/s1
			x = x+5
			x = x*4
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		w6 = s1**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))