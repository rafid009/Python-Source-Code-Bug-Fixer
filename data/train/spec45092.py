import numpy as np 

def function(x):

	o5 = 1
	j3 = x
	paths = []
	try:
		if j3 >= 5:
			x = x*2
			o5 = o5/o5
			x = j3-x
			paths.append(1)
		else:
			o5 = o5*1
			paths.append(2)
		if j3 >= 4:
			x = x-j3
			o5 = 5*o5
			paths.append(3)
		else:
			o5 = o5-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))