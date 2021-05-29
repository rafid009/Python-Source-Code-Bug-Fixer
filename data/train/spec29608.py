import numpy as np 

def function(x):

	v8 = x
	s5 = x
	paths = []
	try:
		if x < 0:
			x = x/5
			paths.append(1)
		else:
			v8 = v8-0
			s5 = v8-5
			v8 = v8+6
			paths.append(2)
		if v8 < 1:
			x = 8-2
			x = 2-x
			x = 2+9
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		v8 = s5**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))