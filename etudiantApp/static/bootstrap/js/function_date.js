function date_heure(idHour,idDate)
{
  date = new Date;
  annee = date.getFullYear();
  moi = date.getMonth();
  mois = new Array('Janvier', 'F&eacute;vrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Ao&ucirc;t', 'Septembre', 'Octobre', 'Novembre', 'D&eacute;cembre');
  j = date.getDate();
  jour = date.getDay();
  jours = new Array('Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi');
  h = date.getHours();
  if(h<10)
  {
    h = "0"+h;
  }
  m = date.getMinutes();
  if(m<10)
  {
    m = "0"+m;
  }
  document.getElementById(idHour).innerHTML = h+':'+m;
  document.getElementById(idDate).innerHTML = jours[jour] + ', ' + j + ' ' + mois[moi] + ' ' + annee;
  setTimeout('date_heure("'+idHour+'","'+idDate+'");','1000');
  return true;
}