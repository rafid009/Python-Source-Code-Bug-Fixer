import numpy as np 

def function(x):

	f7 = 6
	m3 = x
	paths = []
	try:
		if f7 >= 2:
			x = x/8
			x = x+x
			x = f7+x
			paths.append(1)
		else:
			m3 = x/1
			paths.append(2)
		if x <= 5:
			m3 = x+m3
			paths.append(3)
		else:
			x = 8+2
			m3 = f7*5
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))