import numpy as np 

def function(x):

	o3 = 5
	j7 = x
	paths = []
	try:
		if x < 3:
			x = 5+x
			o3 = o3/9
			paths.append(1)
		else:
			x = 0+5
			j7 = j7-6
			x = x-x
			paths.append(2)
		if o3 <= 7:
			x = o3+7
			paths.append(3)
		else:
			o3 = 7*4
			j7 = j7*2
			o3 = 6*j7
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		j7 = j7**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))