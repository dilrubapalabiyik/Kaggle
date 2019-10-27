--
-- PostgreSQL database dump
--

-- Dumped from database version 10.4
-- Dumped by pg_dump version 10.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: player_assists; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_assists (
    season_name text,
    season_type text,
    player_name text,
    team_name text,
    gp double precision,
    minutes double precision,
    assists double precision,
    assist_pts double precision,
    two_pt double precision,
    three_pt double precision,
    at_rim double precision,
    smr double precision,
    lmr double precision,
    c3 double precision,
    ab3 double precision
);


ALTER TABLE public.player_assists OWNER TO postgres;

--
-- Name: player_rebounds; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_rebounds (
    season_name text,
    season_type text,
    player_name text,
    team_name text,
    gamesplayed double precision,
    minutes double precision,
    rebounds double precision,
    defrebounds double precision,
    ftdefrebounds double precision,
    defftreboundpct double precision,
    def2ptrebounds double precision,
    def2ptreboundpct double precision,
    def3ptrebounds double precision,
    def3ptreboundpct double precision,
    deffgreboundpct double precision,
    offrebounds double precision,
    ftoffrebounds double precision,
    offftreboundpct double precision,
    off2ptrebounds double precision,
    off2ptreboundpct double precision,
    off3ptrebounds double precision,
    off3ptreboundpct double precision,
    offfgreboundpct double precision,
    defatrimreboundpct double precision,
    defshortmidrangereboundpct double precision,
    deflongmidrangereboundpct double precision,
    defarc3reboundpct double precision,
    defcorner3reboundpct double precision,
    offatrimreboundpct double precision,
    offshortmidrangereboundpct double precision,
    offlongmidrangereboundpct double precision,
    offarc3reboundpct double precision,
    offcorner3reboundpct double precision
);


ALTER TABLE public.player_rebounds OWNER TO postgres;

--
-- Name: player_scoring; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_scoring (
    season_name text,
    season_type text,
    player_name text,
    team_name text,
    gamesplayed double precision,
    minutes double precision,
    offposs double precision,
    points double precision,
    fg2m double precision,
    fg2a double precision,
    fg2pct double precision,
    fg3m double precision,
    fg3a double precision,
    fg3pct double precision,
    nonheavefg3pct double precision,
    ftsmade double precision,
    ptsassisted2s double precision,
    ptsunassisted2s double precision,
    ptsassisted3s double precision,
    ptsunassisted3s double precision,
    assisted2spct double precision,
    nonputbacksassisted2spct double precision,
    assisted3spct double precision,
    fg3apct double precision,
    shotqualityavg double precision,
    efgpct double precision,
    tspct double precision,
    ptsputbacks double precision,
    fg2ablocked double precision,
    fg2apctblocked double precision,
    fg3ablocked double precision,
    fg3apctblocked double precision,
    usage double precision
);


ALTER TABLE public.player_scoring OWNER TO postgres;

--
-- Name: team_asists; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.team_asists (
    team_name text,
    season_name text,
    season_type text,
    gamesplayed double precision,
    assists double precision,
    assistpoints double precision,
    two_ptassists double precision,
    three_ptassists double precision,
    atrimassists double precision,
    shortmidrangeassists double precision,
    longmidrangeassists double precision,
    corner3assists double precision,
    arc3assists double precision
);


ALTER TABLE public.team_asists OWNER TO postgres;

--
-- Name: team_rebounds; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.team_rebounds (
    season_name text,
    season_type text,
    team_name text,
    gamesplayed double precision,
    rebounds double precision,
    defrebounds double precision,
    ftdefrebounds double precision,
    defftreboundpct double precision,
    def2ptrebounds double precision,
    def2ptreboundpct double precision,
    def3ptrebounds double precision,
    def3ptreboundpct double precision,
    deffgreboundpct double precision,
    offrebounds double precision,
    ftoffrebounds double precision,
    offftreboundpct double precision,
    off2ptrebounds double precision,
    off2ptreboundpct double precision,
    off3ptrebounds double precision,
    off3ptreboundpct double precision,
    offfgreboundpct double precision,
    defatrimreboundpct double precision,
    defshortmidrangereboundpct double precision,
    deflongmidrangereboundpct double precision,
    defarc3reboundpct double precision,
    defcorner3reboundpct double precision,
    offatrimreboundpct double precision,
    offshortmidrangereboundpct double precision,
    offlongmidrangereboundpct double precision,
    offarc3reboundpct double precision,
    offcorner3reboundpct double precision
);


ALTER TABLE public.team_rebounds OWNER TO postgres;

--
-- Name: team_scoring; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.team_scoring (
    team_name text,
    season_name text,
    season_type text,
    gamesplayed double precision,
    offposs double precision,
    points double precision,
    fg2m double precision,
    fg2a double precision,
    fg2pct double precision,
    fg3m double precision,
    fg3a double precision,
    fg3pct double precision,
    nonheavefg3pct double precision,
    ftsmade double precision,
    ptsassisted2s double precision,
    ptsunassisted2s double precision,
    ptsassisted3s double precision,
    ptsunassisted3s double precision,
    assisted2spct double precision,
    nonputbacksassisted2spct double precision,
    assisted3spct double precision,
    fg3apct double precision,
    shotqualityavg double precision,
    efgpct double precision,
    tspct double precision,
    ptsputbacks double precision,
    fg2ablocked double precision,
    fg2apctblocked double precision,
    fg3ablocked double precision,
    fg3apctblocked double precision
);


ALTER TABLE public.team_scoring OWNER TO postgres;

--
-- Data for Name: player_assists; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.player_assists (season_name, season_type, player_name, team_name, gp, minutes, assists, assist_pts, two_pt, three_pt, at_rim, smr, lmr, c3, ab3) FROM stdin;
\.


--
-- Data for Name: player_rebounds; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.player_rebounds (season_name, season_type, player_name, team_name, gamesplayed, minutes, rebounds, defrebounds, ftdefrebounds, defftreboundpct, def2ptrebounds, def2ptreboundpct, def3ptrebounds, def3ptreboundpct, deffgreboundpct, offrebounds, ftoffrebounds, offftreboundpct, off2ptrebounds, off2ptreboundpct, off3ptrebounds, off3ptreboundpct, offfgreboundpct, defatrimreboundpct, defshortmidrangereboundpct, deflongmidrangereboundpct, defarc3reboundpct, defcorner3reboundpct, offatrimreboundpct, offshortmidrangereboundpct, offlongmidrangereboundpct, offarc3reboundpct, offcorner3reboundpct) FROM stdin;
\.


--
-- Data for Name: player_scoring; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.player_scoring (season_name, season_type, player_name, team_name, gamesplayed, minutes, offposs, points, fg2m, fg2a, fg2pct, fg3m, fg3a, fg3pct, nonheavefg3pct, ftsmade, ptsassisted2s, ptsunassisted2s, ptsassisted3s, ptsunassisted3s, assisted2spct, nonputbacksassisted2spct, assisted3spct, fg3apct, shotqualityavg, efgpct, tspct, ptsputbacks, fg2ablocked, fg2apctblocked, fg3ablocked, fg3apctblocked, usage) FROM stdin;
\.


--
-- Data for Name: team_asists; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.team_asists (team_name, season_name, season_type, gamesplayed, assists, assistpoints, two_ptassists, three_ptassists, atrimassists, shortmidrangeassists, longmidrangeassists, corner3assists, arc3assists) FROM stdin;
\.


--
-- Data for Name: team_rebounds; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.team_rebounds (season_name, season_type, team_name, gamesplayed, rebounds, defrebounds, ftdefrebounds, defftreboundpct, def2ptrebounds, def2ptreboundpct, def3ptrebounds, def3ptreboundpct, deffgreboundpct, offrebounds, ftoffrebounds, offftreboundpct, off2ptrebounds, off2ptreboundpct, off3ptrebounds, off3ptreboundpct, offfgreboundpct, defatrimreboundpct, defshortmidrangereboundpct, deflongmidrangereboundpct, defarc3reboundpct, defcorner3reboundpct, offatrimreboundpct, offshortmidrangereboundpct, offlongmidrangereboundpct, offarc3reboundpct, offcorner3reboundpct) FROM stdin;
\.


--
-- Data for Name: team_scoring; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.team_scoring (team_name, season_name, season_type, gamesplayed, offposs, points, fg2m, fg2a, fg2pct, fg3m, fg3a, fg3pct, nonheavefg3pct, ftsmade, ptsassisted2s, ptsunassisted2s, ptsassisted3s, ptsunassisted3s, assisted2spct, nonputbacksassisted2spct, assisted3spct, fg3apct, shotqualityavg, efgpct, tspct, ptsputbacks, fg2ablocked, fg2apctblocked, fg3ablocked, fg3apctblocked) FROM stdin;
\.


--
-- PostgreSQL database dump complete
--

