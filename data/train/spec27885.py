import numpy as np 

def function(x):

	j5 = x
	i3 = x
	x = x
	paths = []
	try:
		if x <= 5:
			j5 = j5+0
			x = 2+x
			x = x/j5
			paths.append(1)
		else:
			i3 = 0/8
			i3 = i3*j5
			paths.append(2)
		if j5 < 8:
			i3 = i3+7
			paths.append(3)
		else:
			j5 = x*x
			j5 = j5+8
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		i3 = j5**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))