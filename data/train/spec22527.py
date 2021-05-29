import numpy as np 

def function(x):

	j2 = 2
	o6 = x
	paths = []
	try:
		if j2 >= 8:
			x = o6-5
			x = j2*0
			o6 = x/o6
			paths.append(1)
		else:
			o6 = 8*2
			paths.append(2)
		if x < 6:
			o6 = o6+o6
			j2 = j2+2
			paths.append(3)
		else:
			x = o6+x
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))