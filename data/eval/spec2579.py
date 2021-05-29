import numpy as np 

def function(x):

	j7 = 3
	v8 = x
	paths = []
	try:
		if x < 7:
			v8 = v8*0
			x = j7-x
			j7 = 6+j7
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if x < 3:
			v8 = 7*9
			v8 = 9*v8
			paths.append(3)
		else:
			v8 = v8-x
			x = x-6
			j7 = 0+1
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		j7 = v8**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))