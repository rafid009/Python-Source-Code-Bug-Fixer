import numpy as np 

def function(x):

	j9 = 2
	u0 = 9
	paths = []
	try:
		if u0 < 6:
			j9 = j9*0
			paths.append(1)
		else:
			x = 5-u0
			j9 = j9/x
			paths.append(2)
		if u0 > 8:
			x = 8/x
			u0 = u0/9
			paths.append(3)
		else:
			x = x/5
			u0 = 7*8
			x = x+1
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