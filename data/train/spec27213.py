import numpy as np 

def function(x):

	j3 = 0
	o7 = 5
	paths = []
	try:
		if j3 >= 4:
			j3 = x*0
			paths.append(1)
		else:
			o7 = o7-6
			o7 = 6/o7
			paths.append(2)
		if j3 <= 2:
			o7 = o7/5
			x = j3+x
			x = x+4
			paths.append(3)
		else:
			o7 = o7-o7
			x = 7+7
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