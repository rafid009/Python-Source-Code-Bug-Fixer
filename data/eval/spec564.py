import numpy as np 

def function(x):

	r1 = x
	i5 = 9
	x = x
	paths = []
	try:
		if r1 < 8:
			r1 = i5-5
			r1 = r1/1
			r1 = r1+i5
			paths.append(1)
		else:
			r1 = 5-2
			r1 = 3-i5
			i5 = 5-i5
			paths.append(2)
		if i5 < 3:
			i5 = i5/7
			paths.append(3)
		else:
			r1 = r1-0
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		r1 = i5**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))