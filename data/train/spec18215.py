import numpy as np 

def function(x):

	o5 = x
	j3 = 6
	paths = []
	try:
		if j3 <= 8:
			o5 = 5*3
			x = 5/x
			j3 = x+x
			paths.append(1)
		else:
			j3 = j3*0
			o5 = o5*o5
			o5 = o5-5
			paths.append(2)
		if j3 > 9:
			o5 = o5-j3
			o5 = 3+o5
			j3 = 9*7
			paths.append(3)
		else:
			o5 = o5-9
			o5 = 2/o5
			j3 = o5-0
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