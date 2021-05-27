import numpy as np 

def function(x):

	o6 = x
	j4 = 9
	paths = []
	try:
		if x <= 3:
			o6 = 9/8
			o6 = o6+j4
			j4 = o6/5
			paths.append(1)
		else:
			o6 = o6*2
			j4 = x*j4
			paths.append(2)
		if o6 >= 7:
			j4 = 5-j4
			x = x*8
			o6 = 5*x
			paths.append(3)
		else:
			j4 = j4+0
			j4 = 1*2
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