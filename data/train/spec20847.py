import numpy as np 

def function(x):

	j3 = x
	t7 = 6
	paths = []
	try:
		if t7 < 4:
			t7 = t7-x
			paths.append(1)
		else:
			x = 5-x
			x = x*j3
			paths.append(2)
		if j3 > 0:
			j3 = j3+2
			t7 = t7-j3
			x = x*3
			paths.append(3)
		else:
			j3 = j3*5
			t7 = 4*t7
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		j3 = t7**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))