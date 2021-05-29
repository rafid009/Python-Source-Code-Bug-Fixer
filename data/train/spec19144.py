import numpy as np 

def function(x):

	i6 = x
	t3 = x
	paths = []
	try:
		if t3 > 4:
			x = x*1
			x = x-2
			x = x+7
			paths.append(1)
		else:
			x = i6+0
			i6 = 6+2
			x = 9*x
			paths.append(2)
		if t3 < 7:
			x = 3*x
			i6 = t3-6
			paths.append(3)
		else:
			i6 = 7*i6
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		i6 = t3**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))