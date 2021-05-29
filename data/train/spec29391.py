import numpy as np 

def function(x):

	o2 = 8
	j4 = 1
	paths = []
	try:
		if j4 <= 9:
			j4 = x-8
			o2 = 6/o2
			o2 = o2*o2
			paths.append(1)
		else:
			o2 = 2+o2
			paths.append(2)
		if x > 3:
			o2 = 1+x
			j4 = 0-0
			paths.append(3)
		else:
			x = x*0
			o2 = 0*o2
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))