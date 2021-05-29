import numpy as np 

def function(x):

	i6 = x
	j9 = 7
	paths = []
	try:
		if i6 < 9:
			j9 = 8/i6
			paths.append(1)
		else:
			x = 8/x
			i6 = 2*i6
			paths.append(2)
		if i6 > 2:
			j9 = 2-j9
			paths.append(3)
		else:
			i6 = i6+0
			x = x*1
			i6 = i6/3
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		j9 = j9**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))