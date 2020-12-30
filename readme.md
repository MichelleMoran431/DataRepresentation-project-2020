
<table>
<thead>
<tr>
<th>Action</th>
<th>Method</th>
<th>URL</th>
<th>Sample Params</th> 
<th>Sample Return</th>
</tr>
</thead>
<tbody>
<tr>
<td>Get All</td>
<td>GET</td>
<td>/groceries</td>
<td>none</td>
<td>[{...},{...},{...}]</td>  
</tr>
<tr>
<td>Find by id</td>
<td>GET</td>
<td>/groceries/id</td>
<td>none</td>
<td>[{"id":"1","Firstname":"xxx"},{"Lastname":"xxx","Postcode":"xxx"}]
</td> 
<tr>
<td>Create</td>
<td>POST</td>
<td>/groceries</td>
<td>{"Firstname":"xxx"},{"Lastname":"xxx","Postcode:"xxx"}</td>
<td>[{"id":"1","Firstname":"xxx"},{"Lastname":"xxx","Postcode":"xxx"}]
</td>
</tr>
<tr>
<td>Update</td>
<td>PUT</td>
<td>/groceries/id</td>
<td>{"Postcode:"xxx"}</td>
<td>[{"id":"1","Firstname":"xxx"},{"Lastname":"xxx","Postcode:"xxx"}]
</td>
</tr>
<td>Delete</td>
<td>DELETE</td>
<td>/groceries/id</td>
<td>none</td>
<td>{"done:"true}
</td>
</tr>  
</tbody>
</table>

