import numpy as np 

def function(x):

	e7 = 4
	u9 = 9
	paths = []
	try:
		if e7 < 3:
			e7 = e7-3
			paths.append(1)
		else:
			u9 = e7*2
			u9 = u9+e7
			e7 = e7*0
			paths.append(2)
		if u9 <= 7:
			e7 = e7*9
			e7 = e7+9
			paths.append(3)
		else:
			u9 = x*8
			u9 = u9/9
			e7 = e7*9
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))