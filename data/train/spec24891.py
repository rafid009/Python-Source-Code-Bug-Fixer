import numpy as np 

def function(x):

	m3 = x
	v5 = 2
	paths = []
	try:
		if x > 3:
			m3 = 1-v5
			x = x+0
			m3 = m3*0
			paths.append(1)
		else:
			x = x+7
			v5 = 0-v5
			paths.append(2)
		if m3 >= 3:
			v5 = v5-x
			v5 = v5*7
			m3 = m3-x
			paths.append(3)
		else:
			v5 = x*v5
			x = 7*x
			x = x*1
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		x = v5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))