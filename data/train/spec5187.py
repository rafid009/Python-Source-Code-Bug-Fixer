import numpy as np 

def function(x):

	k5 = x
	j3 = 6
	paths = []
	try:
		if j3 < 7:
			j3 = x*6
			paths.append(1)
		else:
			j3 = j3+j3
			j3 = 5/j3
			j3 = j3+9
			paths.append(2)
		if x < 4:
			k5 = x-2
			paths.append(3)
		else:
			j3 = j3*0
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		j3 = k5**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))